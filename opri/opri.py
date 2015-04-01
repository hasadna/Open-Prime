#!/usr/bin/env python

import argparse
import sys


class Opri(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Open Prime hosting at your service',
            usage='''opri <command> [<args>]

The most commonly used opri commands are:
   host       start hosting a new project
   list       list the projects
   top        Display the top command from the server
''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def host(self):
        parser = argparse.ArgumentParser(
            description='Host a new project or configure an existing one')
        print 'nothing here yet, just some tutorial code'
        return
        # THIS IS JUST A SAMPLE
        # prefixing the argument with -- means it's optional
        parser.add_argument('--amend', action='store_true')
        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (git) and the subcommand (commit)
        args = parser.parse_args(sys.argv[2:])
        print 'Running git commit, amend=%s' % args.amend

    def list(self):
        parser = argparse.ArgumentParser(
            description='List the known projects')
        print 'nothing here yet, just some tutorial code'
        return
        # THIS IS JUST A SAMPLE
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('repository')
        args = parser.parse_args(sys.argv[2:])
        print 'Running git fetch, repository=%s' % args.repository

    def top(self):
        parser = argparse.ArgumentParser(
            description='ssh to the server and run top')
        print 'nothing here yet'

if __name__ == '__main__':
    Opri()

