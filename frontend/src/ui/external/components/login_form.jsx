import React from "react";
import Editor from "../../../components/editor";
import PrimaryButton from "../../../components/primary_button";

class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { email: "", password: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  // mudanças nos campos de texto
  handleChange(event) {
    // valor do campo
    const value = event.target.value;
    // valor do atributo name
    const name = event.target.name;

    // atualizando o valor
    this.setState({ [name]: value });
  }

  // submeter formulário
  handleSubmit(event) {
    console.log(this.state);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <Editor
          type="email"
          label="Email"
          hint="Informe o seu email"
          identifier="email"
          onChange={this.handleChange}
          value={this.state.email}
        />
        <Editor
          type="password"
          label="Senha"
          hint="Informe a sua senha"
          identifier="password"
          onChange={this.handleChange}
          value={this.state.password}
        />
        <PrimaryButton label="Entrar" />
      </form>
    );
  }
}

export default LoginForm;
