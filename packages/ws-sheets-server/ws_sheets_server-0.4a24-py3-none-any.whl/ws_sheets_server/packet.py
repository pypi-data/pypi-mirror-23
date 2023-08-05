import asyncio
import functools
import os
import pickle
import numpy
import traceback
import logging

import ws_callbacks

import ws_sheets_server

logger = logging.getLogger(__name__)

class Packet(object):
    
    def __init__(self):
        self.callback_post = ws_callbacks.Callbacks()

    def __call__(self, proto):
        pass

    async def post(self, proto):
        logger.debug('{} post'.format(self.__class__.__name__))
        await self.callback_post.acall(proto)

class BookContext(Packet):
    def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        self.call1(proto, book)

    def call1(self, proto, book):
        pass

    async def write_response_book_data(self, proto):
        logger.debug('{} write_response_book_data'.format(self.__class__.__name__))
        book = proto.app.get_book(self.book_id)
        p = await ResponseBookData(self.message_id, self.book_id, book)
        proto.write(p)

    async def write_response_sheet_data(self, sheet_id, proto):
        logger.debug('{} write_response_sheet_data'.format(self.__class__.__name__))
        book = proto.app.get_book(self.book_id)
        sheet = book.sheets[sheet_id]
        p = await ResponseSheetData.create(self.message_id, self.book_id, sheet_id, book, sheet)
        proto.write(p)

class SheetContext(Packet):
    async def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        sheet = book.sheets[self.sheet_id]
        await self.call1(proto, book, sheet)

    async def call1(self, proto, book, sheet):
        pass

    async def write_response_sheet_data(self, proto):
        logger.debug('{} write_response_sheet_data'.format(self.__class__.__name__))
        book = proto.app.get_book(self.book_id)
        sheet = book.sheets[self.sheet_id]
        p = await ResponseSheetData.create(self.message_id, self.book_id, self.sheet_id, book, sheet)
        proto.write(p)

class PacketException(Packet):
    def __init__(self, message):
        self.message = message

class SetCell(SheetContext):
    """
    set cell code string

    :param book_id: book id
    :param sheet_id: sheet id
    :param r: row
    :param c: column
    :param s: code string
    """
    def __init__(self, book_id, sheet_id, r, c, s):
        self.book_id = book_id
        self.sheet_id = sheet_id
        self.r = r
        self.c = c
        self.s = s
    
    async def call1(self, proto, book, sheet):
        logger.debug(repr(self) + '.call1')
        
        await sheet.setitem((self.r, self.c), self.s)

        await book.write()

        await book.calculate()
        
        await self.write_response_sheet_data(proto)

class SetDocs(Packet):
    def __init__(self, book_id, s):
        self.book_id = book_id
        self.s = s
    
    async def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        
        await book.set_docs(self.s)

        await book.write()

class SetScriptPre(BookContext):
    """
    set script_pre string
    """
    def __init__(self, book_id, s):
        super(SetScriptPre, self).__init__()
        self.book_id = book_id
        self.s = s
    
    async def __call__(self, proto):
        logger.debug('{} call s = {}'.format(self.__class__.__name__, self.s))
        
        book = proto.app.get_book(self.book_id)
        
        await book.script_pre.set_string(self.s)

        await book.write()

        await self.post(proto)

class SetScriptPost(BookContext):
    """
    set script_post string

    :param book_id: book_id
    :param s: code string
    """
    def __init__(self, book_id, s):
        super(SetScriptPost, self).__init__()
        self.book_id = book_id
        self.s = s
    
    async def __call__(self, proto):
        logger.debug(repr(self) + '.__call__')

        book = proto.app.get_book(self.book_id)

        await book.script_post.set_string(self.s)

        await book.write()

        await self.post(proto)


class AddColumn(Packet):
    def __init__(self, book_id, sheet_id, i):
        self.book_id = book_id
        self.sheet_id = sheet_id
        self.i = i
    
    def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        sheet = book.sheets[self.sheet_id]
        ret = sheet.add_column(self.i)

        proto.write(ResponseSheetData(self.message_id, self.book_id, self.sheet_id, book, sheet))

class AddRow(Packet):
    def __init__(self, book_id, sheet_id, i):
        self.book_id = book_id
        self.sheet_id = sheet_id
        self.i = i
    
    async def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        sheet = book.sheets[self.sheet_id]
        ret = sheet.add_row(self.i)
        
class GetCellData(Packet):
    def __init__(self, book_id, sheet_id):
        self.book_id = book_id
        self.sheet_id = sheet_id
    
    async def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        sheet = book.sheets[self.sheet_id]

        future = self.run_calculate(proto)

        def callback(future):
            def f(c):
                if c is None:
                    return ws_sheets_server.Cell('','')
                return ws_sheets_server.Cell(c.string,str(c.value))
    
            fv = numpy.vectorize(f, otypes=[ws_sheets_server.Cell])
    
            cells = fv(sheet.cells.cells)
    
            proto.write(ReturnCells(cells))

        future.add_done_callback(callback)

class RequestSheetData(SheetContext):
    def __init__(self, book_id, sheet_id):
        self.book_id = book_id
        self.sheet_id = sheet_id
    
    async def call1(self, proto, book, sheet):
        logger.debug('{} call'.format(self.__class__.__name__))

        await self.write_response_sheet_data(proto)
        
class ResponseBookData(BookContext):
    def __init__(self, response_to, book_id, book):
        self.response_to = response_to

        self.book_id = book_id

        self.sheets = dict((sheet_id, sheet.convert_cells()) for sheet_id, sheet in book.sheets.items())
        
        self.docs = book.docs
        self.script_pre = book.script_pre.string
        self.script_pre_output = book.script_pre.output
        self.script_post = book.script_post.string
        self.script_post_output = book.script_post.output

class ResponseSheetData(SheetContext):
    @classmethod
    async def create(cls, response_to, book_id, sheet_id, book, sheet):
        self = cls()

        await book.calculate()

        self.response_to = response_to
        
        self.book_id = book_id
        self.sheet_id = sheet_id
        
        self.cells = await sheet.convert_cells()
        
        self.docs = book.docs
        self.script_pre = await book.script_pre.string
        self.script_pre_output = await book.script_pre.output
        self.script_post = await book.script_post.string
        self.script_post_output = await book.script_post.output

        logger.debug('  script pre = {}'.format(repr(self.script_pre)))
        logger.debug('  script pre output = {}'.format(repr(self.script_pre_output)))

        return self

    async def __call__(self, proto):
        logger.debug('{} __call__'.format(self.__class__.__name__))
        
        logger.debug('  script pre = {}'.format(repr(self.script_pre)))
        logger.debug('  script pre output = {}'.format(repr(self.script_pre_output)))
        
        proto.temp[self.sheet_id].cells = self.cells
        proto.temp.script_pre.string = self.script_pre
        proto.temp.script_pre.ouptut = self.script_pre_output
        proto.temp.script_post.string = self.script_post
        proto.temp.script_post.ouptut = self.script_post_output


class GetScriptPostOutput(Packet):
    def __init__(self, book_id):
        self.book_id = book_id
    
    def __call__(self, proto):
        book = proto.app.get_book(self.book_id)
        
        proto.write(ReturnScriptPostOutput(self.book_id, book))

class RequestBookNew(Packet):
    def __init__(self): pass
    
    async def __call__(self, proto):
        book_id, book = proto.app.storage.object_new()
        
        proto.write(ResponseBookNew(book_id, self.message_id))

class ResponseBookNew(Packet):
    def __init__(self, book_id, response_to):
        self.book_id = book_id
        self.response_to = response_to
        
class ReturnScriptPostOutput(Packet):
    def __init__(self, book_id, book):
        
        future = self.run_calculate(proto)
        
        def callback(future):
            self.script_post_output = book.script_post.output

        future.add_done_callback(callback)

class ReturnCells(Packet):
    def __init__(self, cells):
        self.cells = cells
    def __call__(self, proto):
        pass


   

