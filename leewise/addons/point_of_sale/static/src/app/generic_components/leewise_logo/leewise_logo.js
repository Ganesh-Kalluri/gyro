/** @leewise-module */

import { Component } from "@leewise/owl";

export class LeewiseLogo extends Component {
    static template = "point_of_sale.LeewiseLogo";
    static props = {
        class: { type: String, optional: true },
        style: { type: String, optional: true },
        monochrome: { type: Boolean, optional: true },
    };
    static defaultProps = {
        class: "",
        style: "",
        monochrome: false,
    };
}
