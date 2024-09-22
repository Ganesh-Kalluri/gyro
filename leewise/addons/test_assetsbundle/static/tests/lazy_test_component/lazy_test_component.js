/** @leewise-module */

import { registry } from "@web/core/registry";
import { Component } from "@leewise/owl";

export class LazyTestComponent extends Component {
    setup() {
        this.props.onCreated();
    }
}
LazyTestComponent.template = "test_assetsbundle.LazyTestComponent";

registry.category("lazy_components").add("LazyTestComponent", LazyTestComponent);
