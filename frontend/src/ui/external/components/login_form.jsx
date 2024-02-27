import { useContext, useState } from "react";
import Editor from "../../../components/editor";
import PrimaryButton from "../../../components/primary_button";
import Constants from "../../../api/constants";
import { AuthContext } from "../../../context/auth_context";
import ErrorCard from "../widgets/error_card";

const LoginForm = () => {
  const [error, setError] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const { dispatch } = useContext(AuthContext);

  const url = `${Constants.base_url}${Constants.login}`;

  const handleLogin = async (e) => {
    e.preventDefault();

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
        dispatch({ type: "AUTHENTICATION", user: json.data });
      } else {
        setError(json.message);
      }
    } catch (error) {
      console.error("Erro durante o login:", error);
      setError(error);
    }
  };

  return (
    <form onSubmit={handleLogin}>
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
        label="Senha"
        hint="Informe a sua senha"
        identifier="password"
        onChange={(e) => setPassword(e.target.value)}
        value={password}
      />
      <PrimaryButton label="Entrar" />
    </form>
  );
};

export default LoginForm;
