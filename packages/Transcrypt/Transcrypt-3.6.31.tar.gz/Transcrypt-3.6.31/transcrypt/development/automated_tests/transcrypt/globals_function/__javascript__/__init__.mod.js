	__nest__ (
		__all__,
		'globals_function', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var sub = __init__ (__world__.globals_function.sub);
					var xxa = 'mainXxa';
					var xxb = 'mainXxb';
					var __iterable0__ = tuple (['xxp', 'xxq']);
					for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
						var py_name = __iterable0__ [__index0__];
						__globals__ (__all__) [py_name] = 'main{}'.format (py_name.capitalize ());
					}
					var f = function () {
						var __iterable0__ = tuple (['xxr', 'xxs']);
						for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
							var py_name = __iterable0__ [__index0__];
							__globals__ (__all__) [py_name] = 'main{}'.format (py_name.capitalize ());
						}
					};
					var run = function (autoTester) {
						f ();
						sub.run (autoTester);
						autoTester.check ('Check main 1', xxa, xxb);
						autoTester.check.apply (null, ['Check main 2'].concat (function () {
							var __accu0__ = [];
							var __iterable0__ = tuple (['xxa', 'xxb', 'xxp', 'xxq', 'xxr', 'xxs']);
							for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
								var py_name = __iterable0__ [__index0__];
								__accu0__.append (__globals__ (__all__) [py_name]);
							}
							return __accu0__;
						} ()));
						autoTester.check ('Check main 3', sub.xxa, sub.xxb, sub.xxp, sub.xxq, sub.xxr, sub.xxs);
						autoTester.check.apply (null, ['Check main 4'].concat (sorted (function () {
							var __accu0__ = [];
							var __iterable0__ = __globals__ (__all__).py_items ();
							for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var key = __left0__ [0];
								var value = __left0__ [1];
								if (key.startswith ('xx')) {
									__accu0__.append (value);
								}
							}
							return __accu0__;
						} ())));
					};
					__pragma__ ('<use>' +
						'globals_function.sub' +
					'</use>')
					__pragma__ ('<all>')
						__all__.f = f;
						__all__.py_name = py_name;
						__all__.run = run;
						__all__.sub = sub;
						__all__.xxa = xxa;
						__all__.xxb = xxb;
					__pragma__ ('</all>')
				}
			}
		}
	);
