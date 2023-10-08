module.exports = {
  // Other ESLint rules and configurations
  rules: {
    'quotes': ['error', 'single'],
    'indent': ['error', 2],
  },
  settings: {
    'import/resolver': {
      node: {
        extensions: ['.js'],
      },
    },
  },
};