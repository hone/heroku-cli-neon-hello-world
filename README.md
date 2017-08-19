# Heroku CLI Hello World with Neon
This is a simple Hello World plugin using [neon](https://github.com/neon-bindings/neon) for the [Heroku CLI](https://github.com/heroku/heroku-cli-hello-world) based off of the [example](https://github.com/heroku/heroku-cli-hello-world) from Heroku. This shows off how one can leverage the power (and stability) of Rust to write the core functionality for a plugin.

## Using
To install this plugin just do a normal plugin install:

```
$ heroku plugins:install heroku-cli-neon-hello-world
```

## Local development

### Native Extensions
In order for users to not need to know about Rust underneath, it uses [node-pre-gyp](https://github.com/neon-bindings/neon) to compile the binaries. It uses TravisCI to compile the 64-bit Linux/OSX binaries, CircleCI to handle the 32-bit binaries, and Appveyor for the 32/64-bit Windows binaries.

The `binding.gyp` file calls `neon build` to compile the native extension as well as move `index.node` into `lib` so it can be found.

### Building
Make sure you have `neon-cli`, `node-pre-gyp` installed:

```
$ npm install -g neon-cli node-pre-gyp
```

To build just do a normal `yarn install`:

```
$ yarn install
```

In order to use this with the heroku CLI, you'll need to [link it](https://devcenter.heroku.com/articles/developing-cli-plugins#installing-the-plugin):

```
$ heroku plugins:link
```
