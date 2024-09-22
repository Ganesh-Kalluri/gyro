/** @leewise-module **/

import * as spreadsheet from "@leewise/o-spreadsheet";

const { parseTokens, iterateAstNodes } = spreadsheet;

/**
 * @typedef {Object} LeewiseFunctionDescription
 * @property {string} functionName Name of the function
 * @property {Array<string>} args Arguments of the function
 *
 * @typedef {Object} Token
 * @property {string} type
 * @property {string} value

 */

/**
 * This function is used to search for the functions which match the given matcher
 * from the given formula
 *
 * @param {Token[]} tokens
 * @param {string[]} functionNames e.g. ["LEEWISE.LIST", "LEEWISE.LIST.HEADER"]
 * @private
 * @returns {Array<LeewiseFunctionDescription>}
 */
export function getLeewiseFunctions(tokens, functionNames) {
    // Parsing is an expensive operation, so we first check if the
    // formula contains one of the function names
    if (!tokens.some((t) => t.type === "SYMBOL" && functionNames.includes(t.value.toUpperCase()))) {
        return [];
    }
    let ast;
    try {
        ast = parseTokens(tokens);
    } catch {
        return [];
    }
    return _getLeewiseFunctionsFromAST(ast, functionNames);
}

/**
 * This function is used to search for the functions which match the given matcher
 * from the given AST
 *
 * @param {Object} ast (see o-spreadsheet)
 * @param {string[]} functionNames e.g. ["LEEWISE.LIST", "LEEWISE.LIST.HEADER"]
 *
 * @private
 * @returns {Array<LeewiseFunctionDescription>}
 */
function _getLeewiseFunctionsFromAST(ast, functionNames) {
    return iterateAstNodes(ast)
        .filter((ast) => ast.type === "FUNCALL" && functionNames.includes(ast.value.toUpperCase()))
        .map((ast) => ({ functionName: ast.value.toUpperCase(), args: ast.args }));
}
