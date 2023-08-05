	__nest__ (
		__all__,
		'unicode_literals', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var unicode_literals = __init__ (__world__.__future__).unicode_literals;
					var run = function (test) {
						test.check ('Hello, world!');
						test.check ('Hello, world!');
					};
					__pragma__ ('<use>' +
						'__future__' +
					'</use>')
					__pragma__ ('<all>')
						__all__.run = run;
						__all__.unicode_literals = unicode_literals;
					__pragma__ ('</all>')
				}
			}
		}
	);
