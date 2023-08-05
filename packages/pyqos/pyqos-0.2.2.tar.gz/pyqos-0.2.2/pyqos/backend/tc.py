#!/usr/bin/env python3
# Author: Anthony Ruhier

from pyqos.tools import launch_command
from pyqos.decorators import multiple_interfaces


@multiple_interfaces
def qdisc(interface, action, algorithm=None, handle=None, parent=None,
          stderr=None, dryrun=False, *args, **kwargs):
    """
    Add/change/replace/replace qdisc

    **kwargs will be used for specific arguments, depending on the algorithm
    used.

    :param action: "add", "replace", "change" or "delete"
    :param interface: target interface
    :param algorithm: algorithm used for this leaf (htb, pfifo, sfq, ...)
    :param handle: handle parameter for tc (default: None)
    :param parent: if is None, the rule will be added as root. (default: None)
    :param stderr: indicates stderr to use during the tc commands execution
    """
    command = ["tc", "qdisc", action, "dev", interface]
    if parent is None:
        command.append("root")
    else:
        command += ["parent", parent]
    if handle is not None:
        command += ["handle", str(handle)]
    if algorithm is not None:
        command.append(algorithm)
    for i, j in sorted(kwargs.items()):
        if j is not None:
            command += [str(i), str(j)]

    launch_command(command, stderr, dryrun)


@multiple_interfaces
def qdisc_add(interface, handle, algorithm, parent=None, *args, **kwargs):
    """
    Add qdisc

    **kwargs will be used for specific arguments, depending on the algorithm
    used.

    :param interface: target interface
    :param algorithm: algorithm used for this leaf (htb, pfifo, sfq, ...)
    :param handle: handle parameter for tc
    :param parent: if is None, the rule will be added as root. (default: None)
    """
    return qdisc(interface, "add", algorithm, handle, parent, *args, **kwargs)


@multiple_interfaces
def qdisc_del(interface, algorithm=None, handle=None, parent=None, *args,
              **kwargs):
    """
    Delete qdisc

    **kwargs will be used for specific arguments, depending on the algorithm
    used.

    :param interface: target interface
    :param algorithm: algorithm used for this leaf (htb, pfifo, sfq, ...)
    :param handle: handle parameter for tc (default: None)
    :param parent: if is None, the rule will be added as root. (default: None)
    """
    return qdisc(interface, "delete", algorithm, handle, parent, *args,
                 **kwargs)


@multiple_interfaces
def qdisc_show(interface=None, show_format=None, dryrun=False):
    """
    Show qdiscs

    :param show_format: option "FORMAT" for tc. (default: None)
        "stats" -> -s
        "details" -> -d
        "raw" -> -r
        "pretty" -> -p
        "iec" -> -i
    :param interface: target interface (default: None)
    """
    formats = {"stats": "-s", "details": "-d", "raw": "-r", "pretty": "-p",
               "iec": "-i"}
    correct_format = formats.get(show_format, None)
    command = ["tc"]
    if show_format is not None:
        command.append(correct_format)
    command += ["qdisc", "show"]
    if interface is not None:
        command += ["dev", interface]
    launch_command(command, dryrun=dryrun)


@multiple_interfaces
def qos_class(interface, action, parent, classid=None, algorithm="htb",
              dryrun=False, *args, **kwargs):
    """
    Add/change/replace/replace class

    **kwargs will be used for specific arguments, depending on the algorithm
    used.
    Parameters need to be in kbit. If the unit isn't indicated, add it
    automagically

    :param action: "add", "replace", "change" or "delete"
    :param interface: target interface
    :param parent: parent class/qdisc
    :param classid: id for the current class (default: None)
    :param algorithm: algorithm used for this class (default: htb)
    """
    command = ["tc", "class", action, "dev", interface, "parent", parent]
    if classid is not None:
        command += ["classid", classid]
    command.append(algorithm)
    if algorithm == "htb":
        for key in ("rate", "ceil"):
            if key in kwargs.keys():
                try:
                    kwargs[key] = str(int(kwargs[key])) + "kbit"
                except:
                    pass
        for key in ("burst", "cburst"):
            if key in kwargs.keys():
                try:
                    kwargs[key] = str(int(kwargs[key])) + "k"
                except:
                    pass
    for i, j in sorted(kwargs.items()):
        if j is not None:
            command += [str(i), str(j)]
    launch_command(command, dryrun=dryrun)


@multiple_interfaces
def qos_class_add(interface, parent, classid, algorithm="htb", **kwargs):
    """
    Add class

    **kwargs will be used for specific arguments, depending on the algorithm
    used.
    Parameters need to be in kbit. If the unit isn't indicated, add it
    automagically

    :param interface: target interface
    :param parent: parent class/qdisc
    :param classid: id for the current class (default: None)
    :param algorithm: algorithm used for this class (default: htb)
    """
    return qos_class(interface, "add", parent, classid, algorithm, **kwargs)


@multiple_interfaces
def qos_class_del(interface, parent, classid=None, algorithm="htb", **kwargs):
    """
    Delete class

    **kwargs will be used for specific arguments, depending on the algorithm
    used.
    Parameters need to be in kbit. If the unit isn't indicated, add it
    automagically

    :param interface: target interface
    :param parent: parent class/qdisc
    :param classid: id for the current class (default: None)
    :param algorithm: algorithm used for this class (default: htb)
    """
    return qos_class(interface, "delete", parent, classid, algorithm, **kwargs)


@multiple_interfaces
def qos_class_show(interface, show_format=None, dryrun=False):
    """
    Show classes

    :param interface: target interface
    :param show_format: option "FORMAT" for tc. (default: None)
        "stats" -> -s
        "details" -> -d
        "raw" -> -r
        "pretty" -> -p
        "iec" -> -i
    """
    formats = {"stats": "-s", "details": "-d", "raw": "-r", "pretty": "-p",
               "iec": "-i"}
    correct_format = formats.get(show_format, None)
    command = ["tc"]
    if show_format is not None:
        command.append(correct_format)
    command += ["class", "show", "dev", interface]
    launch_command(command, dryrun=dryrun)


@multiple_interfaces
def filter(interface, action, prio, handle, flowid, parent=None,
           protocol="all", dryrun=False, *args, **kwargs):
    """
    Add/change/replace/delete filter

    **kwargs will be used for specific arguments, depending on the algorithm
    used.

    :param action: "add", "replace", "change" or "delete"
    :param interface: target interface
    :param prio: priority
    :param handle: filter id
    :param flowid: target class
    :param parent: parent class/qdisc (default: None)
    :param protocol: protocol to filter. (default: "all")
    """
    command = ["tc", "filter", action, "dev", interface]
    if parent is not None:
        command += ["parent", parent]
    command += ["protocol", protocol, "prio", str(prio), "handle", str(handle),
                "fw", "flowid", str(flowid)]
    for i, j in sorted(kwargs.items()):
        if j is not None:
            command += [str(i), str(j)]
    launch_command(command, dryrun=dryrun)


@multiple_interfaces
def filter_add(interface, parent, prio, handle, flowid, protocol="all",
               *args, **kwargs):
    """
    Add filter

    **kwargs will be used for specific arguments, depending on the algorithm
    used.

    :param interface: target interface
    :param parent: parent class/qdisc
    :param prio: priority
    :param handle: filter id
    :param flowid: target class
    :param protocol: protocol to filter (default: "all")
    """
    filter(interface, "add", prio, handle, flowid, parent, protocol,
           *args, **kwargs)


@multiple_interfaces
def filter_del(interface, prio, handle, flowid, parent=None, protocol="all",
               *args, **kwargs):
    """
    Delete filter

    **kwargs will be used for specific arguments, depending on the algorithm
    used.

    :param interface: target interface
    :param prio: priority
    :param handle: filter id
    :param flowid: target class
    :param parent: parent class/qdisc (default: None)
    :param protocol: protocol to filter (default: "all")
    """
    filter(interface, "delete", prio, handle, flowid, parent, protocol,
           *args, **kwargs)


@multiple_interfaces
def filter_show(interface, dryrun=False):
    """
    Show filters

    :param interface: target interface
    """
    launch_command(["tc", "filter", "show", "dev", interface], dryrun=dryrun)
