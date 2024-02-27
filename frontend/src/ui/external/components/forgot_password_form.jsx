import React, {useState} from "react";
import Editor from "../../../components/editor";
import PrimaryButton from "../../../components/primary_button";
import ErrorCard from "../widgets/error_card";
import Constants from "../../../api/constants";

const ForgotPasswordForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");

  const url = `${Constants.base_url}${Constants.reset_password}`;

  const handleForgotPassword = async (e) => {
    e.preventDefault();

    if (confirmPassword != password) {
      setError("Informe a mesma senha.");
    } else {
      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email.trim(),
            password: password.trim(),
          }),
        });

        const json = await response.json();

        if (response.status == 201) {
          console.log(json.message);
        } else {
          setError(json.message);
        }
      } catch (error) {
        console.error("Erro durante a mudança de senha:", error);
        setError(error);
      }
    }
  };

  return (
    <form onSubmit={handleForgotPassword}>
      {error && <ErrorCard message={error} />}
      <Editor
        type="email"
        label="Email"
        hint="Informe o seu email"
        identifier="email"
        onChange={(e) => setEmail(e.target.value)}
        value={email}
      />
      <Editor
        type="password"
        label="Nova senha"
        hint="Informe a sua nova senha"
        identifier="password"
        onChange={(e) => setPassword(e.target.value)}
        value={password}
      />
      <Editor
        type="password"
        label="Confirmar senha"
        hint="Repita a senha informada"
        identifier="confirmPassword"
        onChange={(e) => setConfirmPassword(e.target.value)}
        value={confirmPassword}
      />

      <PrimaryButton label="Salvar" />
    </form>
  );
};

export default ForgotPasswordForm;
