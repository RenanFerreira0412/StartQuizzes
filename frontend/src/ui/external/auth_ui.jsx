import React, { useState } from "react";
import LoginForm from "./components/login_form";
import RegistrationForm from "./components/registration_form";
import ForgotPasswordForm from "./components/forgot_password_form";

class AuthUI extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLogin: true,
      isForgotPassword: false,
    };
  }

  render() {
    const { isLogin, isForgotPassword } = this.state;
    let title, toggleButton, formulary;

    if (isLogin) {
      if (isForgotPassword) {
        title = "Recuperar senha";
        toggleButton = "Voltar";
        formulary = <ForgotPasswordForm />;
      } else {
        title = "Olá, bem-vindo!";
        toggleButton = "Ainda não tem conta? Cadastre-se agora!";
        formulary = <LoginForm />;
      }
    } else {
      title = "Crie uma conta";
      toggleButton = "Já possui uma conta? Entrar";
      formulary = <RegistrationForm />;
    }

    return (
      <div className="auth-ui">
        <div className="auth-ui-container">
          <p>{title}</p>

          {formulary}

          {!isForgotPassword && isLogin && (
            <button
              className="forgot-password-btn"
              onClick={() =>
                this.setState({ isForgotPassword: !isForgotPassword })
              }
            >
              Esqueceu sua senha?
            </button>
          )}
        </div>
        <div className="auth-ui-container">
          <button
            className="toggleButton"
            onClick={() =>
              isForgotPassword
                ? this.setState({ isForgotPassword: !isForgotPassword })
                : this.setState({ isLogin: !isLogin })
            }
          >
            {toggleButton}
          </button>
        </div>
      </div>
    );
  }
}

export default AuthUI;
