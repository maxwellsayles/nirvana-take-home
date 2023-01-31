# Nirvana Take-home Project

## Overview

The problem describes a REST request and response, rather than a concrete API.  As such, I chose to mock the API and implement a test suite, rather than a concrete program, as a solution to the problem. From the top level directory, the test suite can be run using

> $ python -m unittest

You can typecheck the source using

> $ mypy .

The solution presented here declares abstract classes for an `Endpoint` and `Reducer`, and a concrete implementation of `EndpointReducerProxy` as well as two reducers. The proxy class takes a collection of endpoints and then reduces the results using the provided `Reducer`. This makes the framework flexible both in the concrete implementation of the `Endpoint` and `Reducer`. The logic specifying how results are combined can be customized by deriving from `Reducer` and using the `EndpointReducerProxy`.

The test suite provides a `MockEndpoint` that returns constant results. There are tests for the example input and "average" reducer from the problem description. There's also a test for a generalized `LambdaReducer` that permits inline logic for reducing results.

## Design Choices

- The problem description says the API should take a `member_id`, however, since this argument is ignored by this contrived implementation, I chose to ignore this detail in the API.
- Invoking a REST API is typically an asynchronous operation, so I chose to implement the `Endpoint` using `async`. The mock returns a constant, so `async` is unnecessary in this case, but captures the asynchronous expectation of the API.
- The `EndpointReducerProxy` uses `asyncio.gather` to make endpoint requests concurrently.
- Combining results is functionally equivalent to reducing a collection to a single result, and this logic is already provided by `functools.reduce`. Technically, the framework could have been written to take a list of endpoints and a function for `functools.reduce` to combine results. However, I chose to provide an abstract `Reducer` class for several reasons: doing so explicitly encapsulates the logic for how to reduce a collection of results, makes the logic easily reusable, and exposes the complete collection for reduction (rather than as an acculator and single element).
  - However, for fun, I also provide a `LambdaReducer` that exposes the functionality of `functools.reduce` directly and allows you to write the reduction logic inline. (See the `testLambda` test in `test_endpoint_reducer_proxy.py` for an example.)
- Unit tests are collocated with the code being tested (i.e. `tests` and `reducers/tests`). This encourages test creation and maintenance since they are more visible alongside code being written.


## Possible Considerations

- Calls to a REST API may fail. These may be intermittent or permanent, and neither are considered in the solution here. Intermittent errors may be retried or accounted for some other way when reducing the result. Permanent errors should be surfaced by the system especially if the system takes a hard dependency on the external resource. They may also be accounted for when reducing the result if the system is permitted to continue.
- `Endpoint` could be defined to return multiple results. This is a generalization of calling multiple endpoints and then performing an operation on the results, and allows for stacking of combinators. For example, one combinator might be to select all results with an `oop_max < 1000` and the results would then be passed through a subsequent combinator to select the result with the smallest `deductible`. Unless the system truly needs this flexibility, this seems like overkill. :)

