import "./styles/App.css";
import AuthUI from "./ui/external/auth_ui";
import HomeUI from "./ui/internal/home_ui";
import { AuthContext } from "./context/auth_context";
import { useContext } from "react";

function App() {
  const { currentUser } = useContext(AuthContext);
  return <>{currentUser ? <HomeUI /> : <AuthUI />}</>;
}

export default App;
