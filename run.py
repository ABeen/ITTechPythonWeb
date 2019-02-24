from optparse import OptionParser
from datetime import datetime
from pprint import pprint
from termcolor import colored

from web import run


def _show_info(app):
    """ 显示系统信息
    """
    severinfo = "Server start on port {0} ...".format(app.settings['port'])
    starttime = "Start time: {0}".format(datetime.now().isoformat(" "))
    print(colored(severinfo, "green", attrs=["bold", "blink"]))
    print(colored(starttime, "green", attrs=["bold", "blink"]))

    print("Parameters:")
    for k in sorted(app.settings.keys()):
        if k.startswith("__"):
            continue
        print("  {0:<20} : {1}".format(k, app.settings[k]))

    print("Handlers:")
    handlers = sorted(app.handlers, key=lambda h: h[0])
    pprint(handlers, width='90')

    if app.settings.get("debug"):
        print(colored("WARNING", "red", attrs=["bold", "blink"]), ": Debug Mode is True!!!")


def _get_opt():
    parser = OptionParser("%prog [options]", version="%prog v0.9")
    parser.add_option("--port", dest="port", type="int", default=8888, help="Listen port.")
    parser.add_option("--debug", dest="debug", action="store_true", default=True, help="Debug mode.")

    return parser.parse_args()


def main():
    opts, args = _get_opt()
    run(debug=opts.debug, port=opts.port, callback=_show_info)


if __name__ == '__main__':
    main()
