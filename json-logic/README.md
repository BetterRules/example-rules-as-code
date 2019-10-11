# JSON Logic

This encodes the rule about beards in
a [JSON Logic](http://jsonlogic.com/) format.

JSON Logic can be parsed in many different languages -
see [their website](http://jsonlogic.com/) for more details.
The tests are written using the
[JS parser](https://github.com/jwadhams/json-logic-js/),
which has been pulled down into the `logic.js` file.

The logic is in `beard_definition.json`.
See `test/beard_definition_test.js` for an example of how to call it.

To run tests:
`node test/beard_definition_test.js`
