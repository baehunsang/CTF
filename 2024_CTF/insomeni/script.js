var popenAddr = Module.findExportByName('libc.so.6', 'popen')
var popen = new NativeFunction(popenAddr, 'pointer', ['pointer','pointer'])

var fgetsAddr = Module.findExportByName('libc.so.6', 'fgets')
var fgets = new NativeFunction(fgetsAddr, 'pointer', ['pointer','int','pointer'])
var cmd_args = Memory.alloc(1024);
var cmd_type = Memory.alloc(1024);
var path = Memory.alloc(120024);

Memory.writeUtf8String(cmd_args, "base64 -w 0 /usr/local/bin/tetris")
Memory.writeUtf8String(cmd_type, "r")

var fp = popen(cmd_args, cmd_type)
fgets(path, 120024, fp)
Memory.readUtf8String(path)
