/** @leewise-module */

import { Component } from "@leewise/owl";

export class PartnerLine extends Component {
    static template = "point_of_sale.PartnerLine";

    get highlight() {
        return this._isPartnerSelected ? "highlight active" : "";
    }
    get _isPartnerSelected() {
        return this.props.partner === this.props.selectedPartner;
    }
}
