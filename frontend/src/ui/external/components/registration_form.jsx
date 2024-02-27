import { useState, useContext } from "react";
import Editor from "../../../components/editor";
import PrimaryButton from "../../../components/primary_button";
import { AuthContext } from "../../../context/auth_context";
import ErrorCard from "../widgets/error_card";
import Constants from "../../../api/constants";

const RegistrationForm = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");

  const { dispatch } = useContext(AuthContext);

  const url = `${Constants.base_url}${Constants.register}`;

  const handleRegistration = async (e) => {
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
            name: name.trim(),
            email: email.trim(),
            password: password.trim(),
          }),
        });

        const json = await response.json();

        if (response.status == 201) {
          dispatch({ type: "AUTHENTICATION", user: json.data });
        } else {
          setError(json.message);
        }
      } catch (error) {
        console.error("Erro durante o cadastro:", error);
        setError(error);
      }
    }
  };

  return (
    <form onSubmit={handleRegistration}>
      {error && <ErrorCard message={error} />}
      <Editor
        type="text"
        label="Nome"
        hint="Informe o seu nome"
        identifier="name"
        onChange={(e) => setName(e.target.value)}
        value={name}
      />
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
        label="Senha"
        hint="Informe a sua senha"
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
      <PrimaryButton label="Cadastrar" />
    </form>
  );
};

export default RegistrationForm;
