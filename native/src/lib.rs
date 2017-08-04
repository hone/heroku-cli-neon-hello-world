#[macro_use]
extern crate neon;

use neon::vm::{Call, JsResult};
use neon::js::JsString;

fn hello(call: Call) -> JsResult<JsString> {
    let scope = call.scope;
    let name = call.arguments.require(scope, 0).unwrap().check::<JsString>().unwrap().value();
    Ok(JsString::new(scope, &format!("hello {}!", name)).unwrap())
}

register_module!(m, {
    m.export("hello", hello)
});
