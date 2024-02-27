class Constants {
  // caminho base
  static base_url = import.meta.env.VITE_BASE_URL;

  static login = import.meta.env.VITE_LOGIN;
  static register = import.meta.env.VITE_REGISTER;
  static logout = import.meta.env.VITE_LOGOUT;
  static reset_password = import.meta.env.VITE_RESET_PASSWORD;
  static delete_account = import.meta.env.VITE_DELETE_ACCOUNT;
  static current_user = import.meta.env.VITE_CURRENT_USER;
}

export default Constants;
