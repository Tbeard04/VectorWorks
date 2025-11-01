import { render, screen } from '@testing-library/react';
import App from './App';

test('renders VectorWorks brand', () => {
  render(<App />);
  const brand = screen.getByText(/VectorWorks/i);
  expect(brand).toBeInTheDocument();
});

