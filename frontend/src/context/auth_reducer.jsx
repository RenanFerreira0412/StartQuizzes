const AuthReducer = (state, action) => {
  switch (action.type) {
    case "AUTHENTICATION": {
      return {
        currentUser: action.user,
      };
    }
    case "LOGOUT": {
      return {
        currentUser: null,
      };
    }

    default:
      return state;
  }
};

export default AuthReducer;
