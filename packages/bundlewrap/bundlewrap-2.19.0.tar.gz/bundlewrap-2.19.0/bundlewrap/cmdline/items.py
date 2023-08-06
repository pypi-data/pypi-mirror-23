# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os import makedirs
from os.path import dirname, exists, join
from sys import exit

from ..utils.cmdline import get_item, get_node
from ..utils.statedict import statedict_to_json
from ..utils.text import force_text, mark_for_translation as _, red
from ..utils.ui import io


def write_preview(file_item, base_path):
    """
    Writes the content of the given file item to the given path.
    """
    file_path = join(base_path, file_item.name.lstrip("/"))
    dir_path = dirname(file_path)
    if not exists(dir_path):
        makedirs(dir_path)
    with open(file_path, 'wb') as f:
        f.write(file_item.content)


def bw_items(repo, args):
    node = get_node(repo, args['node'], adhoc_nodes=args['adhoc_nodes'])
    if args['file_preview']:
        item = get_item(node, "file:{}".format(args['file_preview']))
        if (
            item.attributes['content_type'] in ('any', 'base64', 'binary') or
            item.attributes['delete'] is True
        ):
            io.stderr(_(
                "{x} cannot preview {file} on {node} (unsuitable content_type or deleted)"
            ).format(x=red("!!!"), file=item.id, node=node.name))
            exit(1)
        else:
            io.stdout(item.content.decode(item.attributes['encoding']), append_newline=False)
    elif args['file_preview_path']:
        if exists(args['file_preview_path']):
            io.stderr(_(
                "not writing to existing path: {path}"
            ).format(path=args['file_preview_path']))
            exit(1)
        for item in sorted(node.items):
            if not item.id.startswith("file:"):
                continue
            if item.attributes['content_type'] == 'any':
                io.stderr(_(
                    "skipping file with 'any' content {filename}..."
                ).format(filename=item.name))
                continue
            if item.attributes['content_type'] == 'binary':
                io.stderr(_(
                    "skipping binary file {filename}..."
                ).format(filename=item.name))
                continue
            if item.attributes['delete']:
                io.stderr(_(
                    "skipping file with 'delete' flag {filename}..."
                ).format(filename=item.name))
                continue
            io.stdout(_("writing {path}...").format(path=join(
                args['file_preview_path'],
                item.name.lstrip("/"),
            )))
            write_preview(item, args['file_preview_path'])
    elif args['item']:
        item = get_item(node, args['item'])
        if args['show_sdict']:
            statedict = item.sdict()
        else:
            statedict = item.cdict()
        if statedict is None:
            io.stdout("REMOVE")
        else:
            if args['attr']:
                io.stdout(repr(statedict[args['attr']]))
            else:
                io.stdout(statedict_to_json(statedict, pretty=True))
    else:
        for item in sorted(node.items):
            if args['show_repr']:
                io.stdout(force_text(repr(item)))
            else:
                io.stdout(force_text(str(item)))
