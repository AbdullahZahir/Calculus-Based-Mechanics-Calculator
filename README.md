# Calculus-Based-Mechanics-Calculator
Classical Mechanics Calculator is a terminal-based Python solver spanning 10 chapters of university-level Physics I — from Kinematics to Calculus-Based Oscillations — implementing 80+ equations across every major domain of classical mechanics without any external physics libraries. At its core, the system runs a dynamic known-variable resolution engine built around a centralized knowns dictionary, which is pre-populated through intelligent scenario detection before pattern-matching against conditional equation chains to select the correct algebraic rearrangement for any valid combination of inputs. The architecture is deliberately modular: each physics domain is fully encapsulated with isolated state and per-session resets, while repeated behaviors like input validation, solution formatting, and context-specific guidance are abstracted into reusable helper functions. Notably, the tipsAndNotes() function uses Python's inspect.stack() for runtime stack-frame introspection, dynamically dispatching chapter-specific notes based on its calling context — eliminating redundant logic across all 10 modules. Navigation is handled through a recursive showChapter() engine that maintains persistent session state, allowing users to move fluidly between chapters without restarting the program.


Capabilities Summary
Chapter 1 — Kinematics

Solves all 5 classical kinematic equations for any unknown: displacement, initial/final velocity, acceleration, and time
Detects constant-velocity and at-rest scenarios automatically

Chapter 2 — Forces (Newtonian Dynamics)

Implements Newton's Second Law (F = ma) in direct and impulse-expanded form
Solves for friction, normal force, net force (multi-force summation), weight, and coefficient of friction (μ)
Scenario detection for free fall, constant velocity, and flat-surface normal force equivalence

Chapter 3 — Linear Momentum & Impulse

Solves for momentum, impulse, and change in momentum across 5 equation forms
Handles the full impulse-momentum equivalence chain: J = Δp = FΔt = mvf − mvi

Chapter 4 — Collisions (Conservation of Momentum)

Separate solvers for elastic (m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f) and inelastic (m₁v₁ᵢ + m₂v₂ᵢ = (m₁+m₂)vf) collisions
Solves for any unknown: either mass, either initial velocity, either final velocity, or momentum values
At-rest scenario detection for both objects

Chapter 5 — Energy

Solves for kinetic energy, gravitational potential energy, elastic potential energy, and Hooke's Law
System-aware scenario detection: excludes irrelevant energy terms (e.g., no spring, no vertical displacement, object at rest)

Chapter 6 — Work & Power

Four sub-modes: kinetic work, gravitational potential work, elastic potential work, and general work/power
Supports angled force application via degree-to-radian conversion and cosine projection
Solves for power, horsepower conversion, and energy-time relationships

Chapter 7 — Rotational Kinematics

Full rotational analog of Chapter 1: all 5 rotational kinematic equations solved for any unknown (θ, ωᵢ, ωf, α, t)
Arc length relationship (s = rθ) with radius and angular displacement solving
Constant angular velocity and at-rest detection

Chapter 8 — Rotational Dynamics

Implements τ = Iα (Newton's Second Law for rotation), torque from tangential force, angular momentum (L = Iω), change in angular momentum, rotational kinetic energy (½Iω²), point-mass moment of inertia (I = mr²), centripetal force, and tangential velocity
Conservation of angular momentum scenario flagging

Chapter 9 — Oscillations (Simple Harmonic Motion)

Three sub-modes: spring-mass SHM, simple pendulum, and general SHM
Solves for position x(t), velocity v(t), and acceleration a(t) using the full cosine model with phase constant φ
Period and frequency from angular frequency, spring constant, mass, and pendulum length
Maximum velocity from amplitude, total oscillator energy (E = ½kA²), and velocity from position via energy conservation
Phase constant pre-population for standard initial conditions (φ = 0 and φ = π/2)

Chapter 10 — Calculus-Based Physics

Four sub-modes grounded in derivative and integral relationships:

Calculus Kinematics: derives x(t), v(t), a(t) from integration/differentiation of constant-acceleration equations with initial conditions
Calculus Rotational Kinematics: full rotational analog using θ(t), ω(t), α(t) with calculus derivations
Calculus Work-Energy: work as the integral of force over displacement (W = ∫F dx), KE from the work-energy theorem, spring PE from integrating Hooke's Law (∫kx dx), and conservation of total mechanical energy
Calculus Oscillations: evaluates x(t) = A·cos(ωt+φ), v(t) = dx/dt, and a(t) = d²x/dt² as explicit derivative relationships; recovers amplitude from initial conditions and angular frequency from the SHM differential equation identity a = −ω²x
