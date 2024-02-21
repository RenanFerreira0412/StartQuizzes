import React from "react";
import Editor from "../../../components/editor";
import PrimaryButton from "../../../components/primary_button";

class RegistrationForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { name: "", email: "", password: "", confirmPassword: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    // valor do campo
    const value = event.target.value;
    // valor do atributo name
    const name = event.target.name;

    // atualizando o valor
    this.setState({ [name]: value });
  }

  handleSubmit(event) {
    console.log(this.state);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <Editor
          type="text"
          label="Nome"
          hint="Informe o seu nome"
          identifier="name"
          onChange={this.handleChange}
          value={this.state.name}
        />
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
        <Editor
          type="password"
          label="Confirmar senha"
          hint="Repita a senha informada"
          identifier="confirmPassword"
          onChange={this.handleChange}
          value={this.state.confirmPassword}
        />
        <PrimaryButton label="Cadastrar" />
      </form>
    );
  }
}

export default RegistrationForm;
