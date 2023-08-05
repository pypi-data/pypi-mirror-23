	__nest__ (
		__all__,
		'print_function', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var print_function = __init__ (__world__.__future__).print_function;
					var run = function (test) {
						test.check ('from __future__ import print_function works');
					};
					__pragma__ ('<use>' +
						'__future__' +
					'</use>')
					__pragma__ ('<all>')
						__all__.print_function = print_function;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
