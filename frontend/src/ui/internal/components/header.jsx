import { AuthContext } from "../../../context/auth_context";
import { useContext } from "react";
import Constants from "../../../api/constants";

const Header = () => {
  const { currentUser, dispatch } = useContext(AuthContext);

  const url = `${Constants.base_url}${Constants.logout}/${currentUser.id}`;

  const handleLogout = async () => {
    try {
      const response = await fetch(url, {
        method: "PUT",
      });

      const json = await response.json();

      if (response.status == 201) {
        dispatch({ type: "LOGOUT", user: null });
      }
    } catch (error) {
      console.error("Erro durante o cadastro:", error);
    }
  };

  return (
    <div>
      <p>Olá {currentUser.name}</p>

      <div>
        <button>Meus Quizzes</button>
        <button>Criar Quiz</button>
        <button onClick={handleLogout}>Sair</button>
      </div>
    </div>
  );
};

export default Header;
