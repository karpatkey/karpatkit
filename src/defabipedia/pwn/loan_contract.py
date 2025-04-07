[
    {
        "inputs": [
            {"internalType": "address", "name": "_hub", "type": "address"},
            {"internalType": "address", "name": "_loanToken", "type": "address"},
            {"internalType": "address", "name": "_config", "type": "address"},
            {"internalType": "address", "name": "_revokedNonce", "type": "address"},
            {"internalType": "address", "name": "_categoryRegistry", "type": "address"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "addr", "type": "address"},
            {"internalType": "bytes32", "name": "tag", "type": "bytes32"},
        ],
        "name": "AddressMissingHubTag",
        "type": "error",
    },
    {"inputs": [], "name": "CallerNotLOANTokenHolder", "type": "error"},
    {"inputs": [], "name": "CallerNotVault", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "current", "type": "uint256"},
            {"internalType": "uint256", "name": "expiration", "type": "uint256"},
        ],
        "name": "Expired",
        "type": "error",
    },
    {"inputs": [], "name": "IncompleteTransfer", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "current", "type": "uint256"},
            {"internalType": "uint256", "name": "limit", "type": "uint256"},
        ],
        "name": "InterestAPROutOfBounds",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "current", "type": "uint256"},
            {"internalType": "uint256", "name": "limit", "type": "uint256"},
        ],
        "name": "InvalidDuration",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidExtensionCaller", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "duration", "type": "uint256"},
            {"internalType": "uint256", "name": "limit", "type": "uint256"},
        ],
        "name": "InvalidExtensionDuration",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "allowed", "type": "address"},
            {"internalType": "address", "name": "current", "type": "address"},
        ],
        "name": "InvalidExtensionSigner",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "bytes32", "name": "current", "type": "bytes32"},
            {"internalType": "bytes32", "name": "expected", "type": "bytes32"},
        ],
        "name": "InvalidLenderSpecHash",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "uint8", "name": "category", "type": "uint8"},
            {"internalType": "address", "name": "addr", "type": "address"},
            {"internalType": "uint256", "name": "id", "type": "uint256"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "InvalidMultiTokenAsset",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "signer", "type": "address"},
            {"internalType": "bytes32", "name": "digest", "type": "bytes32"},
        ],
        "name": "InvalidSignature",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "length", "type": "uint256"}],
        "name": "InvalidSignatureLength",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "address", "name": "sourceOfFunds", "type": "address"}],
        "name": "InvalidSourceOfFunds",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint40", "name": "timestap", "type": "uint40"}],
        "name": "LoanDefaulted",
        "type": "error",
    },
    {"inputs": [], "name": "LoanNotAutoclaimable", "type": "error"},
    {"inputs": [], "name": "LoanNotRepaid", "type": "error"},
    {"inputs": [], "name": "LoanNotRunning", "type": "error"},
    {"inputs": [], "name": "LoanRepaid", "type": "error"},
    {"inputs": [], "name": "LoanRunning", "type": "error"},
    {"inputs": [], "name": "NonExistingLoan", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "addr", "type": "address"},
            {"internalType": "uint256", "name": "nonceSpace", "type": "uint256"},
            {"internalType": "uint256", "name": "nonce", "type": "uint256"},
        ],
        "name": "NonceNotUsable",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "currentBorrower", "type": "address"},
            {"internalType": "address", "name": "newBorrower", "type": "address"},
        ],
        "name": "RefinanceBorrowerMismatch",
        "type": "error",
    },
    {"inputs": [], "name": "RefinanceCollateralMismatch", "type": "error"},
    {"inputs": [], "name": "RefinanceCreditMismatch", "type": "error"},
    {
        "inputs": [{"internalType": "uint8", "name": "categoryValue", "type": "uint8"}],
        "name": "UnsupportedCategory",
        "type": "error",
    },
    {"inputs": [], "name": "UnsupportedTransferFunction", "type": "error"},
    {
        "inputs": [{"internalType": "address", "name": "addr", "type": "address"}],
        "name": "VaultTransferSameSourceAndDestination",
        "type": "error",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "extensionHash",
                "type": "bytes32",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "proposer",
                "type": "address",
            },
            {
                "components": [
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {
                        "internalType": "address",
                        "name": "compensationAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "compensationAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint40", "name": "duration", "type": "uint40"},
                    {"internalType": "uint40", "name": "expiration", "type": "uint40"},
                    {"internalType": "address", "name": "proposer", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nonceSpace",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "nonce", "type": "uint256"},
                ],
                "indexed": false,
                "internalType": "struct PWNSimpleLoan.ExtensionProposal",
                "name": "proposal",
                "type": "tuple",
            },
        ],
        "name": "ExtensionProposalMade",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": true,
                "internalType": "bool",
                "name": "defaulted",
                "type": "bool",
            },
        ],
        "name": "LOANClaimed",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "proposalHash",
                "type": "bytes32",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "proposalContract",
                "type": "address",
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "refinancingLoanId",
                "type": "uint256",
            },
            {
                "components": [
                    {"internalType": "address", "name": "lender", "type": "address"},
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {"internalType": "uint32", "name": "duration", "type": "uint32"},
                    {
                        "components": [
                            {
                                "internalType": "enum MultiToken.Category",
                                "name": "category",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "assetAddress",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "id",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct MultiToken.Asset",
                        "name": "collateral",
                        "type": "tuple",
                    },
                    {
                        "components": [
                            {
                                "internalType": "enum MultiToken.Category",
                                "name": "category",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "assetAddress",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "id",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct MultiToken.Asset",
                        "name": "credit",
                        "type": "tuple",
                    },
                    {
                        "internalType": "uint256",
                        "name": "fixedInterestAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint24",
                        "name": "accruingInterestAPR",
                        "type": "uint24",
                    },
                    {
                        "internalType": "bytes32",
                        "name": "lenderSpecHash",
                        "type": "bytes32",
                    },
                    {
                        "internalType": "bytes32",
                        "name": "borrowerSpecHash",
                        "type": "bytes32",
                    },
                ],
                "indexed": false,
                "internalType": "struct PWNSimpleLoan.Terms",
                "name": "terms",
                "type": "tuple",
            },
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "sourceOfFunds",
                        "type": "address",
                    }
                ],
                "indexed": false,
                "internalType": "struct PWNSimpleLoan.LenderSpec",
                "name": "lenderSpec",
                "type": "tuple",
            },
            {
                "indexed": false,
                "internalType": "bytes",
                "name": "extra",
                "type": "bytes",
            },
        ],
        "name": "LOANCreated",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": false,
                "internalType": "uint40",
                "name": "originalDefaultTimestamp",
                "type": "uint40",
            },
            {
                "indexed": false,
                "internalType": "uint40",
                "name": "extendedDefaultTimestamp",
                "type": "uint40",
            },
        ],
        "name": "LOANExtended",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            }
        ],
        "name": "LOANPaidBack",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "indexed": false,
                "internalType": "struct MultiToken.Asset",
                "name": "asset",
                "type": "tuple",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "poolAdapter",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "pool",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
        ],
        "name": "PoolSupply",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "indexed": false,
                "internalType": "struct MultiToken.Asset",
                "name": "asset",
                "type": "tuple",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "poolAdapter",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "pool",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
        ],
        "name": "PoolWithdraw",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "indexed": false,
                "internalType": "struct MultiToken.Asset",
                "name": "asset",
                "type": "tuple",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "origin",
                "type": "address",
            },
        ],
        "name": "VaultPull",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "indexed": false,
                "internalType": "struct MultiToken.Asset",
                "name": "asset",
                "type": "tuple",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "beneficiary",
                "type": "address",
            },
        ],
        "name": "VaultPush",
        "type": "event",
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "indexed": false,
                "internalType": "struct MultiToken.Asset",
                "name": "asset",
                "type": "tuple",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "origin",
                "type": "address",
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "beneficiary",
                "type": "address",
            },
        ],
        "name": "VaultPushFrom",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "ACCRUING_INTEREST_APR_DECIMALS",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "ACCRUING_INTEREST_APR_DENOMINATOR",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "DOMAIN_SEPARATOR",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "EXTENSION_PROPOSAL_TYPEHASH",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_ACCRUING_INTEREST_APR",
        "outputs": [{"internalType": "uint40", "name": "", "type": "uint40"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_EXTENSION_DURATION",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MINUTES_IN_YEAR",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MIN_EXTENSION_DURATION",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MIN_LOAN_DURATION",
        "outputs": [{"internalType": "uint32", "name": "", "type": "uint32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "VERSION",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "categoryRegistry",
        "outputs": [
            {
                "internalType": "contract IMultiTokenCategoryRegistry",
                "name": "",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "loanId", "type": "uint256"}],
        "name": "claimLOAN",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "config",
        "outputs": [{"internalType": "contract PWNConfig", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "proposalContract",
                        "type": "address",
                    },
                    {"internalType": "bytes", "name": "proposalData", "type": "bytes"},
                    {
                        "internalType": "bytes32[]",
                        "name": "proposalInclusionProof",
                        "type": "bytes32[]",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct PWNSimpleLoan.ProposalSpec",
                "name": "proposalSpec",
                "type": "tuple",
            },
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "sourceOfFunds",
                        "type": "address",
                    }
                ],
                "internalType": "struct PWNSimpleLoan.LenderSpec",
                "name": "lenderSpec",
                "type": "tuple",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "refinancingLoanId",
                        "type": "uint256",
                    },
                    {"internalType": "bool", "name": "revokeNonce", "type": "bool"},
                    {"internalType": "uint256", "name": "nonce", "type": "uint256"},
                ],
                "internalType": "struct PWNSimpleLoan.CallerSpec",
                "name": "callerSpec",
                "type": "tuple",
            },
            {"internalType": "bytes", "name": "extra", "type": "bytes"},
        ],
        "name": "createLOAN",
        "outputs": [{"internalType": "uint256", "name": "loanId", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {
                        "internalType": "address",
                        "name": "compensationAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "compensationAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint40", "name": "duration", "type": "uint40"},
                    {"internalType": "uint40", "name": "expiration", "type": "uint40"},
                    {"internalType": "address", "name": "proposer", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nonceSpace",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "nonce", "type": "uint256"},
                ],
                "internalType": "struct PWNSimpleLoan.ExtensionProposal",
                "name": "extension",
                "type": "tuple",
            },
            {"internalType": "bytes", "name": "signature", "type": "bytes"},
        ],
        "name": "extendLOAN",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "name": "extensionProposalsMade",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {
                        "internalType": "address",
                        "name": "compensationAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "compensationAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint40", "name": "duration", "type": "uint40"},
                    {"internalType": "uint40", "name": "expiration", "type": "uint40"},
                    {"internalType": "address", "name": "proposer", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nonceSpace",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "nonce", "type": "uint256"},
                ],
                "internalType": "struct PWNSimpleLoan.ExtensionProposal",
                "name": "extension",
                "type": "tuple",
            }
        ],
        "name": "getExtensionHash",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "loanId", "type": "uint256"}],
        "name": "getLOAN",
        "outputs": [
            {"internalType": "uint8", "name": "status", "type": "uint8"},
            {"internalType": "uint40", "name": "startTimestamp", "type": "uint40"},
            {"internalType": "uint40", "name": "defaultTimestamp", "type": "uint40"},
            {"internalType": "address", "name": "borrower", "type": "address"},
            {"internalType": "address", "name": "originalLender", "type": "address"},
            {"internalType": "address", "name": "loanOwner", "type": "address"},
            {"internalType": "uint24", "name": "accruingInterestAPR", "type": "uint24"},
            {
                "internalType": "uint256",
                "name": "fixedInterestAmount",
                "type": "uint256",
            },
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "internalType": "struct MultiToken.Asset",
                "name": "credit",
                "type": "tuple",
            },
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "internalType": "struct MultiToken.Asset",
                "name": "collateral",
                "type": "tuple",
            },
            {
                "internalType": "address",
                "name": "originalSourceOfFunds",
                "type": "address",
            },
            {"internalType": "uint256", "name": "repaymentAmount", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "sourceOfFunds",
                        "type": "address",
                    }
                ],
                "internalType": "struct PWNSimpleLoan.LenderSpec",
                "name": "lenderSpec",
                "type": "tuple",
            }
        ],
        "name": "getLenderSpecHash",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
        "name": "getStateFingerprint",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "hub",
        "outputs": [{"internalType": "contract PWNHub", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "enum MultiToken.Category",
                        "name": "category",
                        "type": "uint8",
                    },
                    {
                        "internalType": "address",
                        "name": "assetAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "id", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "internalType": "struct MultiToken.Asset",
                "name": "asset",
                "type": "tuple",
            }
        ],
        "name": "isValidAsset",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "loanMetadataUri",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "loanId", "type": "uint256"}],
        "name": "loanRepaymentAmount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "loanToken",
        "outputs": [{"internalType": "contract PWNLOAN", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {
                        "internalType": "address",
                        "name": "compensationAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "compensationAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint40", "name": "duration", "type": "uint40"},
                    {"internalType": "uint40", "name": "expiration", "type": "uint40"},
                    {"internalType": "address", "name": "proposer", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nonceSpace",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "nonce", "type": "uint256"},
                ],
                "internalType": "struct PWNSimpleLoan.ExtensionProposal",
                "name": "extension",
                "type": "tuple",
            }
        ],
        "name": "makeExtensionProposal",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "onERC1155BatchReceived",
        "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "operator", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "onERC1155Received",
        "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "operator", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "onERC721Received",
        "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "loanId", "type": "uint256"}],
        "name": "repayLOAN",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "revokedNonce",
        "outputs": [{"internalType": "contract PWNRevokedNonce", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}],
        "name": "supportsInterface",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "loanId", "type": "uint256"},
            {"internalType": "uint256", "name": "creditAmount", "type": "uint256"},
            {"internalType": "address", "name": "loanOwner", "type": "address"},
        ],
        "name": "tryClaimRepaidLOAN",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
