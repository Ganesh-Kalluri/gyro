/** @leewise-module **/

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { SignListController } from "@sign/views/sign_list/sign_list_controller";

export const signListView = {
    ...listView,
    Controller: SignListController,
};
registry.category("views").add("sign_list", signListView);
