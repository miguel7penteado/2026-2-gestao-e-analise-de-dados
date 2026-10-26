X_test = np.array([
    [4.5],   # Saúde
    [6.5],   # Bela Vista
    [9.0]    # Vila Olímpia
])

y_test = np.array([
    28,
    34,
    42
])

y_pred = modelo.predict(X_test)

for x, real, previsto in zip(X_test, y_test, y_pred):
    print(
        f"x={x[0]:.1f} | "
        f"real={real:.2f} | "
        f"previsto={previsto:.2f}"
    )
