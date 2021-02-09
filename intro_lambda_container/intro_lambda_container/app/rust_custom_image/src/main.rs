// """
// Name: main.rs
// Created by: Masato Shima
// Created on: 2021/02/07
// Description: Sample lambda application.
// """

use lambda_runtime::{error::HandlerError, lambda, Context};
use serde_derive::{Serialize, Deserialize};

#[derive(Deserialize, Clone)]
struct CustomEvent {
    message: String,
}

#[derive(Serialize, Clone)]
struct CustomOutput {
    message: String,
}

fn main() {
    lambda!(lambda_handler);
}

fn lambda_handler(_: CustomEvent, _: Context) -> Result<CustomOutput, HandlerError> {
    Ok(CustomOutput{
        message: String::from("Hello Lambda Container ! (Rust Custom Image)"),
    })
}

// End
