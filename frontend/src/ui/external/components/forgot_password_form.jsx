import React from "react";
import Editor from "../../../components/editor";
import PrimaryButton from "../../../components/primary_button";

class ForgotPasswordForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      password: "",
      confirmPassword: "",
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    // valor do campo de texto
    const value = event.target.value;

    // valor do atributo name
    const name = event.target.name;

    // atualizando o valor
    this.setState({ [name]: value });
  }

  handleSubmit(event) {
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
          label="Nova senha"
          hint="Informe a sua nova senha"
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

        <PrimaryButton label="Salvar" />
      </form>
    );
  }
}

export default ForgotPasswordForm;
