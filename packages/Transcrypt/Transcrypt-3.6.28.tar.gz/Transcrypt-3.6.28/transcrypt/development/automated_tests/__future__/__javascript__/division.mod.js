	__nest__ (
		__all__,
		'division', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var division = __init__ (__world__.__future__).division;
					var _check = function (x, test) {
						if (x == int (x)) {
							var x = int (x);
						}
						if (isinstance (x, float)) {
							var x = str (x).__getslice__ (0, 15, 1);
						}
						test.check (x);
					};
					var run = function (test) {
						var check = (function __lambda__ (x) {
							return _check (x, test);
						});
						for (var i = 1; i < 10; i++) {
							check (42 / i);
							check (i / 42);
							check (Math.floor (42 / i));
							check (Math.floor (i / 42));
						}
					};
					__pragma__ ('<use>' +
						'__future__' +
					'</use>')
					__pragma__ ('<all>')
						__all__._check = _check;
						__all__.division = division;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
