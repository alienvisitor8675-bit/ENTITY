```tla
\begin======================================================================

\section{Digital Identity and Credentials}

\subsection{Modeling with TLA+}

\begin{code}

\begin{figure}
\begin{tla}
\begin{align*}
\text{--- Digital Identity and Credentials Model in TLA+ ---}\\
\\
\text{Variables:}\\
\text{--- User: Set of (Subject, Isser)}\\
\text{User}\ \in\ \{ \text{Subject} \times \text{Isser} \}^?\\
\\
\text{--- Issuer: Set of (Subject, Isser, Claim)}\\
\text{Issuer}\ \in\ \{ \text{Subject} \times \text{Isser} \times \text{Claim} \}^?\\
\\
\text{--- Verification: Set of (Subject, Isser, VerifiedClaim)}\\
\text{Verification}\ \in\ \{ \text{Subject} \times \text{Isser} \times \text{VerifiedClaim} \}^?\\
\\
\text{Invariants:}\\
\\
\text{For all } v \in \text{Verification}:\\
\text{If } v \in \text{Verification}, \text{ then } v.Isser \in \text{Issuer}.v.Subject.\\
\\
\text{For all } v \in \text{Verification}:\\
\text{If } v \in \text{Verification}, \text{ then } \langle v.Subject, v.Isser \rangle \in \text{User}.\\
\\
\end{align*}
\end{figure}
\end{code}

\begin{align*}
\text{--- End of Model ---}\\
\\
\text{Explanation:}\\
\text{This TLA+ model captures the relationship between users, issuers, and claims in a digital identity system. The invariants ensure that a claim is only considered verified if the issuer is recognized by the user for that subject. The model supports further analysis of identity and verification properties.}
\end{align*}
\end{tla}
\end{align*}
\end{code}

\end{figure}
</think>

```tla
\begin{figure}
\begin{tla}
\begin{align*}
\text{--- Digital Identity and Credentials Model in TLA+ ---}\\
\\
\text{Variables:}\\
\text{--- User: Set of (Subject, Isser)}\\
\text{User}\ \in\ \{ \text{Subject} \times \text{Isser} \}^?\\
\\
\text{--- Issuer: Set of (Subject, Isser, Claim)}\\
\text{Issuer}\ \in\ \{ \text{Subject} \times \text{Isser} \times \text{Claim} \}^?\\
\\
\text{--- Verification: Set of (Subject, Isser, VerifiedClaim)}\\
\text{Verification}\ \in\ \{ \text{Subject} \times \text{Isser} \times \text{VerifiedClaim} \}^?\\
\\
\text{Invariants:}\\
\\
\text{For all } v \in \text{Verification}:\\
\text{If } v \in \text{Verification}, \text{ then } v.Isser \in \text{Issuer}.v.Subject.\\
\\
\text{For all } v \in \text{Verification}:\\
\text{If } v \in \text{Verification}, \text{ then } \langle v.Subject, v.Isser \rangle \in \text{User}.\\
\\
\end{align*}
\end{figure}
\end{tla}
```