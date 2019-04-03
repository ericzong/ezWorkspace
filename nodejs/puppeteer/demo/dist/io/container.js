"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.container = undefined;

var _awilix = require("awilix");

// Create the container and set the injectionMode to PROXY (which is also the default).
const container = exports.container = (0, _awilix.createContainer)({
    injectionMode: _awilix.InjectionMode.PROXY
});

// Load modules
container.loadModules([`${__dirname}/../../plugins/**/*.js`, `${__dirname}/../../services/**/*.js`], {
    formatName: 'camelCase',
    resolverOptions: {
        lifetime: _awilix.Lifetime.SINGLETON,
        register: _awilix.asClass
    }
});
//# sourceMappingURL=container.js.map