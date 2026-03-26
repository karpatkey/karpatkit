from inspect import getmembers
from types import ModuleType

from . import (  # noqa
    _1inch,
    aave_v3,
    angle,
    arrakis,
    aura,
    balancer,
    balancer_v3,
    centrifuge,
    chainlink,
    compound_v3,
    convex,
    cowswap_signer,
    curve,
    dolomite,
    enzyme,
    ethena,
    etherfi,
    gas_replenisher,
    gmx,
    gnosis,
    helper_contracts,
    hop,
    lido,
    m0,
    maker,
    maverick,
    merkle,
    morpho,
    mu,
    multisend,
    nexus_mutual,
    olas,
    opus_pool,
    origin,
    pendle,
    pods,
    pooltogether,
    rocket_pool,
    sky,
    sommelier,
    spark,
    stakedao,
    stakewise_v3,
    swap_pools,
    swapr_v3,
    tokens,
    uniswap_v2,
    uniswap_v3,
    xdai_bridge,
)
from .types import *  # noqa
from .types import Blockchain, ContractSpec

# Extract all ContractSpecs from the imported modules
# and build an in-memory database
_CONTRACT_SPECS_BY_CHAIN_ADDR = {}

protocol_modules = [m for m in locals().values() if isinstance(m, ModuleType)]
for module in protocol_modules:
    multichain_contract_specs = getattr(module, "ContractSpecs", None)
    if multichain_contract_specs:
        for chain, specs_class in multichain_contract_specs.items():
            contract_specs = getmembers(specs_class, predicate=lambda x: isinstance(x, ContractSpec))
            for _, spec in contract_specs:
                _CONTRACT_SPECS_BY_CHAIN_ADDR[(chain, spec.address)] = spec


def get_contract_spec(chain: Blockchain, address: str):
    """Search for a ContractSpec in the database"""
    return _CONTRACT_SPECS_BY_CHAIN_ADDR[(chain, address)]
