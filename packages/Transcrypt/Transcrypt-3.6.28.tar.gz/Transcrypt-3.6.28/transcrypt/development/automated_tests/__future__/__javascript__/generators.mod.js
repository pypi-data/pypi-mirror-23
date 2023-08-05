	__nest__ (
		__all__,
		'generators', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var generators = __init__ (__world__.__future__).generators;
					var run = function (test) {
						for (var i = 0; i < 10; i++) {
							test.check (i);
						}
					};
					__pragma__ ('<use>' +
						'__future__' +
					'</use>')
					__pragma__ ('<all>')
						__all__.generators = generators;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
