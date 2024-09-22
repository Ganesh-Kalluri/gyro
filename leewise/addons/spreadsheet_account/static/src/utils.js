/** @leewise-module **/
import { getLeewiseFunctions } from "@spreadsheet/helpers/leewise_functions_helpers";

/**
 * @typedef {import("@spreadsheet/helpers/leewise_functions_helpers").Token} Token
 * @typedef  {import("@spreadsheet/helpers/leewise_functions_helpers").LeewiseFunctionDescription} LeewiseFunctionDescription
 */

/**
 * @param {Token[]} tokens
 * @returns {number}
 */
export function getNumberOfAccountFormulas(tokens) {
    return getLeewiseFunctions(tokens, ["LEEWISE.BALANCE", "LEEWISE.CREDIT", "LEEWISE.DEBIT"]).length;
}

/**
 * Get the first Account function description of the given formula.
 *
 * @param {Token[]} tokens
 * @returns {LeewiseFunctionDescription | undefined}
 */
export function getFirstAccountFunction(tokens) {
    return getLeewiseFunctions(tokens, ["LEEWISE.BALANCE", "LEEWISE.CREDIT", "LEEWISE.DEBIT"])[0];
}
