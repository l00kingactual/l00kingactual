from bayes_opt import BayesianOptimization

def bayesian_optimization(input_shape, num_classes, x_train, y_train, build_fn, logger):
    def evaluate(num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate):
        model = build_fn(
            input_shape=(input_shape,),
            num_classes=num_classes,
            num_layers=int(num_layers),
            units_0=int(units_0),
            dropout_0=dropout_0,
            units_1=int(units_1),
            dropout_1=dropout_1,
            learning_rate=learning_rate
        )
        history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, verbose=0)
        accuracy = history.history['val_accuracy'][-1]
        return accuracy

    pbounds = {
        'num_layers': (2, 10),
        'units_0': (16, 1024),
        'dropout_0': (0.0, 0.75),
        'units_1': (32, 512),
        'dropout_1': (0.0, 0.25),
        'learning_rate': (1e-6, 1e-1),
    }

    optimizer = BayesianOptimization(
        f=evaluate,
        pbounds=pbounds,
        random_state=1
    )

    logger.debug("Starting Bayesian Optimization")
    optimizer.maximize(init_points=10, n_iter=30)

    logger.debug(f"Best Bayesian Optimization: {optimizer.max}")

    # Extracting the best hyperparameters
    best_hyperparams = optimizer.max['params']
    best_hyperparams['num_layers'] = int(best_hyperparams['num_layers'])
    best_hyperparams['units_0'] = int(best_hyperparams['units_0'])
    best_hyperparams['units_1'] = int(best_hyperparams['units_1'])

    return best_hyperparams
