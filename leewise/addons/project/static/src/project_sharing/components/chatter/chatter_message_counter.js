/** @leewise-module */

import { Component } from "@leewise/owl";

export class ChatterMessageCounter extends Component { }

ChatterMessageCounter.props = {
    count: Number,
};
ChatterMessageCounter.template = 'project.ChatterMessageCounter';
