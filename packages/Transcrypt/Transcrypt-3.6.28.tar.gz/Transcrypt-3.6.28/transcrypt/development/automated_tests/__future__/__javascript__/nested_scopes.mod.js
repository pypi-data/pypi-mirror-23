	__nest__ (
		__all__,
		'nested_scopes', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var nested_scopes = __init__ (__world__.__future__).nested_scopes;
					var run = function (test) {
						var foo = function () {
							var x = 42;
							var bar = function () {
								test.check (x);
							};
							bar ();
						};
						foo ();
					};
					__pragma__ ('<use>' +
						'__future__' +
					'</use>')
					__pragma__ ('<all>')
						__all__.nested_scopes = nested_scopes;
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
