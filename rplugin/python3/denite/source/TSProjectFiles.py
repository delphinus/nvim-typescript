#! /usr/bin/env python3

from .base import Base


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.vim = vim
        self.name = 'TSProjectFiles'
        self.kind = 'file'

    def convertToCandidate(self, symbols):
        return list(map(lambda symbol: {
            'text':  symbol,
        }, symbols))

    def gather_candidates(self, context):
        response = self.vim.funcs.TSGetProjectInfoFunc()
        if response is None:
            return []
        candidates = self.convertToCandidate(response['fileNames'])
        return list(map(lambda symbol: {
            'word': symbol['text'],
            'action__path': symbol['text']
        }, candidates))
