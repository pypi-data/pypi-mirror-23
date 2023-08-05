	(function () {
		var division = {};
		var generators = {};
		var nested_scopes = {};
		var print_function = {};
		var sys = {};
		var unicode_literals = {};
		__nest__ (sys, '', __init__ (__world__.sys));
		try {
			sys.path.append ('.');
		}
		catch (__except0__) {
			// pass;
		}
		__nest__ (division, '', __init__ (__world__.division));
		__nest__ (generators, '', __init__ (__world__.generators));
		__nest__ (nested_scopes, '', __init__ (__world__.nested_scopes));
		__nest__ (print_function, '', __init__ (__world__.print_function));
		__nest__ (unicode_literals, '', __init__ (__world__.unicode_literals));
		var AutoTester = __init__ (__world__.org.transcrypt.autotester).AutoTester;
		var atester = AutoTester ();
		atester.run (division, 'division');
		atester.run (generators, 'generators');
		atester.run (nested_scopes, 'nested_scope');
		atester.run (print_function, 'print_function');
		atester.run (unicode_literals, 'unicode_literals');
		atester.done ();
		__pragma__ ('<use>' +
			'division' +
			'generators' +
			'nested_scopes' +
			'org.transcrypt.autotester' +
			'print_function' +
			'sys' +
			'unicode_literals' +
		'</use>')
		__pragma__ ('<all>')
			__all__.AutoTester = AutoTester;
			__all__.atester = atester;
		__pragma__ ('</all>')
	}) ();
