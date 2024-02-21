function Editor({ label, hint, identifier, type, onChange, value }) {
  return (
    <>
      <div className="form-group">
        <label htmlFor={identifier} className="form-group-label">
          {label}
        </label>
        <input
          type={type}
          id={identifier}
          name={identifier}
          placeholder={hint}
          value={value}
          onChange={onChange}
          required
        />
        <span className="helperText">{hint}</span>
      </div>
    </>
  );
}

export default Editor;
