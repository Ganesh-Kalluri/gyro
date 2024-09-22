/** @leewise-module **/

import { Component } from "@leewise/owl";

export class WarningNotification extends Component {
    static template = "website_sale.warningNotification";
    static props = {
        warning: [String, { toString: Function }],
    }
}
