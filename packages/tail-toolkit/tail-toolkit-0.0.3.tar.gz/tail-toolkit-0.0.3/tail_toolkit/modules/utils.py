#!/usr/bin/env python

import os
import pkgutil


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def click_get_command_choice(command, conf):
        opts = ['']
        if command in conf.cli:
            for opt in conf.cli[command]['commands']:
                opts.append(opt)

        return opts

    @staticmethod
    def docstring_parameter(*sub):
        def dec(obj):
            obj.__doc__ = pkgutil.get_data("tail_toolkit", os.path.join(sub[0].sett['C_HELPS_FILES'], obj.func_name + ".txt"))
            #obj.__doc__ = "HELPAAAAAAA"
            return obj
        return dec

    @staticmethod
    def click_validate_required_options(ctx,conf):
        if ctx.info_name in conf.cli:
            if ctx.params['action'] in conf.cli[ctx.info_name]['commands']:
                for check in conf.cli[ctx.info_name]['commands'][ctx.params['action']]:
                    if ctx.params[check] is None or ctx.params[check] is False:
                        print("The option '--" + check + "' is required");
                        exit(1)

