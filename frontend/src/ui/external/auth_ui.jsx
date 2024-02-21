import { useState } from "react";
import LoginForm from "./components/login_form";
import RegistrationForm from "./components/registration_form";
import ForgotPasswordForm from "./components/forgot_password_form";

function AuthUI() {
  // controlar as telas de autenticação
  const [isLogin, setIsLogin] = useState(true);
  // controlar a tela de esqueceu sua senha
  const [isForgotPassword, setIsForgotPassword] = useState(false);

  var formulary, title, toggleButton;

  // controlando o conteúdo da página de autenticação
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
    <>
      <div className="auth-ui">
        <p className="auth-ui-title">StartQuizzes</p>
        <div className="auth-ui-container">
          {title}

          <button
            className="toggleButton"
            onClick={() =>
              isForgotPassword
                ? setIsForgotPassword(!isForgotPassword)
                : setIsLogin(!isLogin)
            }
          >
            {toggleButton}
          </button>
          {formulary}

          {!isForgotPassword && isLogin && (
            <button
              className="forgot-password-btn"
              onClick={() => setIsForgotPassword(!isForgotPassword)}
            >
              Esqueceu sua senha?
            </button>
          )}
        </div>
      </div>
    </>
  );
}

export default AuthUI;
