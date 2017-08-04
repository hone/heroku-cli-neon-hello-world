// @flow
import {Command, flags} from 'cli-engine-heroku'
import addon from '../../native'

export default class HelloWorld extends Command {
  static topic = 'hello'
  static command = 'world'
  static description = 'say hi'
  static flags = {
    name: flags.string({description: 'name to say hello to'})
  }

  async run () {
    let name = this.flags.name || 'world'
    this.out.log(addon.hello(name))
  }
}
