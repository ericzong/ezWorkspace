import { createContainer, InjectionMode, Lifetime, asClass } from "awilix";

// Create the container and set the injectionMode to PROXY (which is also the default).
export const container = createContainer({
    injectionMode: InjectionMode.PROXY
});

// Load modules
container.loadModules([
    `${__dirname}/../../plugins/**/*.js`,
    `${__dirname}/../../services/**/*.js`
], {
    formatName: 'camelCase',
    resolverOptions: {
        lifetime: Lifetime.SINGLETON,
        register: asClass
    }
})
