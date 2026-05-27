def test_import_package():
    import foresightgraph
    assert hasattr(foresightgraph, "__version__")
    assert foresightgraph.hello() == "hello from foresightgraph"