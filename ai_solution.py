```tla
\begin{figure}
\begin{tla}
\begin{align*}
\text{{--- Digital Identity and Credentials Model in TLA+ ---}}

\text{{Constants:}}
\text{{Subject}}, \text{{Isser}}, \text{{Claim}}, \text{{VerifiedClaim}} \in \{\text{...}\}

\text{{Variables:}}

\text{{User}} \in \{{ \text{{Subject}} \times \text{{Isser}} \}}^?

\text{{Issuer}} \in \{{ \text{{Subject}} \times \text{{ Isser}} \times \text{{Claim}} \}}^?

\text{{Verification}} \in \{{ \text{{Subject}} \times \text{{ Isser}} \times \text{{ VerifiedClaim}} \}}^?

\text{{Invariants:}}

\forall v \in \text{{Verification}}. \langle v.Subject, v.Isser, v.Claim \rangle \in \text{{Issuer}}

\forall v \in \text{{Verification}}. \langle v.Subject, v.Isser \rangle \in \text{{User}}

\end{align*}
\end{tla}
\end{figure}
```