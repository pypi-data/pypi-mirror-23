	__nest__ (
		__all__,
		'async_await', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					
					    function waitAWhile (aTime) {
					      return new Promise (resolve => {
					        setTimeout (() => {
					          resolve (aTime);
					        }, 1000 * aTime);
					      });
					    }
					
					var run = function (autoTester) {
						var counter = 0;
						var f = async function () {
							autoTester.check ('f0');
							await waitAWhile (2);
							autoTester.check ('f1');
							counter++;
						};
						var g = async function () {
							autoTester.check ('g0');
							await waitAWhile (2);
							autoTester.check ('g1');
							counter++;
						};
						autoTester.check ('BEGIN async/await test');
						if (__envir__.executor_name == __envir__.transpiler_name) {
							f ();
							g ();
							g ();
							f ();
						}
						else {
							var eventLoop = asyncio.get_event_loop ();
							var tasks = list ([eventLoop.create_task (f ()), eventLoop.create_task (g ()), eventLoop.create_task (g ()), eventLoop.create_task (f ())]);
							var waitingTasks = asyncio.wait (tasks);
							eventLoop.run_until_complete (waitingTasks);
							eventLoop.close ();
						}
						autoTester.check ('END async/await test');
					};
					__pragma__ ('<all>')
						__all__.run = run;
					__pragma__ ('</all>')
				}
			}
		}
	);
