# Converter Tools

```shell
pip install km3pipe
```

```shell
# JGandalf -> HDF5
tohdf5 --aa-format=jevt_jgandalf some_jgandalf.aa.root
```

```shell
ORCA RecoLNS -> HDF5

tohdf5 --aa-format=ancient_recolns \
  --aa-lib=$SPS/lquinn/sandbox/aa-recoLNSlowE-prod2016/bin/reco_v0r9_standalone.so \
  some_recolns.root
```

```shell
# HDF5 -> ROOT
hdf2root foo.h5
```
